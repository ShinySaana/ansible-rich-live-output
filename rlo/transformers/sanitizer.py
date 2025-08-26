from . import BaseRLOTransformer

# TODO: Re-do all this.

# See https://en.wikipedia.org/wiki/ANSI_escape_code#C0_control_codes for some of those codes
BLACKLISTED_BYTES = {
    0x07: "<BEL>",
    0x08: "<BS>",
    # Tab (\t, 0x9 / 9) is kept because it cannot by itself overwrite any data on a well-implemented terminal emulator screen.
    # Line feed (\n, 0xA / 10) is kept because it cannot by itself overwrite any data on a well-implemented terminal emulator screen.
    0x0C: "<FF>",
    0x0D: "<CR>",
    0x1B: "<ESC>",
    0x7F: "<DEL>",
}

class Sanitizer(BaseRLOTransformer):
    @classmethod
    def priority() -> int:
        return 9999

    def transform(self, input: str) -> str:
        current = input
        for byte_to_replace, replace_with in BLACKLISTED_BYTES.items():
            current = current.replace(chr(byte_to_replace), replace_with)
        return current
