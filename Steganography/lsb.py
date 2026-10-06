"""
Nama Program : Algoritma encoding & decoding LSB
Nama         : Ibnaty Farah Rabbany
NPM          : 140810240022
Tanggal      : 6 Oktober 2026
"""

from pathlib import Path
from PIL import Image

# Number of bits used from each RGB channel.
LSB_BITS = 1

# Header stores the message length in bits.
HEADER_BITS = 32


def text_to_bits(message):
    """Convert UTF-8 text into a sequence of 0/1 bits."""
    data = message.encode("utf-8")
    return [
        (byte >> bit) & 1
        for byte in data
        for bit in range(7, -1, -1)
    ]


def bits_to_bytes(bits):
    """Convert a sequence of bits into bytes."""
    if len(bits) % 8 != 0:
        raise ValueError("Jumlah bit tidak merupakan kelipatan 8.")

    result = bytearray()

    for i in range(0, len(bits), 8):
        byte = 0
        for bit in bits[i:i + 8]:
            byte = (byte << 1) | bit
        result.append(byte)

    return bytes(result)


def bits_to_text(bits):
    """Convert bits back into UTF-8 text."""
    data = bits_to_bytes(bits)
    return data.decode("utf-8")


def int_to_bits(value, bit_length=HEADER_BITS):
    """Convert an integer to a fixed-length bit sequence."""
    if value < 0 or value >= 2 ** bit_length:
        raise ValueError("Nilai terlalu besar untuk header.")

    return [
        (value >> bit) & 1
        for bit in range(bit_length - 1, -1, -1)
    ]


def bits_to_int(bits):
    """Convert a bit sequence into an integer."""
    value = 0

    for bit in bits:
        value = (value << 1) | bit

    return value


def get_capacity(image):
    """Return the maximum payload capacity in bits."""
    width, height = image.size
    return width * height * 3 * LSB_BITS


def check_capacity(image, payload_bits):
    """Check whether the image can store the payload."""
    required_bits = HEADER_BITS + len(payload_bits)
    capacity = get_capacity(image)

    if required_bits > capacity:
        max_bytes = max(0, (capacity - HEADER_BITS) // 8)
        raise ValueError(
            "Pesan terlalu panjang untuk gambar.\n"
            f"Kapasitas maksimum sekitar {max_bytes} byte."
        )


def embed_bits(image, bits):
    """Embed bits sequentially into the LSB of RGB channels."""
    pixels = list(image.getdata())
    bit_index = 0

    for pixel_index, pixel in enumerate(pixels):
        r, g, b = pixel

        channels = [r, g, b]

        for channel_index in range(3):
            if bit_index >= len(bits):
                break

            channels[channel_index] = (
                (channels[channel_index] & 0b11111110)
                | bits[bit_index]
            )
            bit_index += 1

        pixels[pixel_index] = tuple(channels)

        if bit_index >= len(bits):
            break

    return pixels


def encode_message(cover_path, output_path, message):
    """Encode a text message into a cover image."""
    cover = Image.open(cover_path).convert("RGB")

    payload_bits = text_to_bits(message)
    check_capacity(cover, payload_bits)

    # Store message length in bytes in a 32-bit header.
    message_length = len(message.encode("utf-8"))
    header_bits = int_to_bits(message_length)

    all_bits = header_bits + payload_bits
    pixels = embed_bits(cover, all_bits)

    stego = Image.new("RGB", cover.size)
    stego.putdata(pixels)
    stego.save(output_path, format="PNG")


def extract_bits(image, count):
    """Extract a given number of LSBs sequentially from RGB channels."""
    bits = []

    for r, g, b in image.getdata():
        for channel in (r, g, b):
            bits.append(channel & 1)

            if len(bits) == count:
                return bits

    raise ValueError("Data pada gambar tidak cukup untuk diekstraksi.")


def decode_message(stego_path):
    """Extract and decode the hidden UTF-8 message."""
    stego = Image.open(stego_path).convert("RGB")

    header_bits = extract_bits(stego, HEADER_BITS)
    message_length = bits_to_int(header_bits)

    message_bits = extract_bits(
        stego,
        HEADER_BITS + (message_length * 8)
    )[HEADER_BITS:]

    return bits_to_text(message_bits)


def get_user_path(prompt, default_path=None):
    """Read a path from the user, optionally using a default path."""
    if default_path is None:
        value = input(prompt).strip()
    else:
        value = input(f"{prompt} [{default_path}]: ").strip()
        value = value or str(default_path)

    return Path(value)


def encode_menu():
    """Handle the encode menu."""
    cover_path = get_user_path(
        "Masukkan path cover image",
        Path("images") / "cover.png"
    )

    message = input("Masukkan pesan rahasia: ")

    output_path = get_user_path(
        "Masukkan path output",
        Path("output") / "stego.png"
    )

    try:
        encode_message(cover_path, output_path, message)

        image = Image.open(cover_path).convert("RGB")
        capacity = get_capacity(image)
        message_size = len(message.encode("utf-8"))

        print("\nEncoding berhasil!")
        print(f"Cover image : {cover_path}")
        print(f"Output      : {output_path}")
        print(f"Pesan       : {message}")
        print(f"Ukuran pesan: {message_size} byte")
        print(f"Kapasitas   : {(capacity - HEADER_BITS) // 8} byte")
    except (FileNotFoundError, ValueError, OSError) as error:
        print(f"\nError: {error}")


def decode_menu():
    """Handle the decode menu."""
    stego_path = get_user_path(
        "Masukkan path stego image",
        Path("output") / "stego.png"
    )

    try:
        message = decode_message(stego_path)

        print("\nDecoding berhasil!")
        print(f"Stego image : {stego_path}")
        print(f"Pesan rahasia:\n{message}")
    except (FileNotFoundError, ValueError, UnicodeDecodeError, OSError) as error:
        print(f"\nError: {error}")


def show_menu():
    """Display the main program menu."""
    print("\n" + "=" * 44)
    print("          LSB STEGANOGRAPHY")
    print("=" * 44)
    print("1. Encode Message")
    print("2. Decode Message")
    print("3. Exit")
    print("=" * 44)


def main():
    """Run the application."""
    while True:
        show_menu()
        choice = input("Pilih menu: ").strip()

        if choice == "1":
            encode_menu()
        elif choice == "2":
            decode_menu()
        elif choice == "3":
            print("\nProgram selesai.")
            break
        else:
            print("\nPilihan tidak valid. Silakan pilih 1, 2, atau 3.")


if __name__ == "__main__":
    main()
