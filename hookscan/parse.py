"""Load an email file and pull out the headers an analyst checks first."""
from email import policy
from email.parser import BytesParser


def load_email(path):
    """Read a .eml file and return a parsed message object."""
    with open(path, "rb") as f:
        return BytesParser(policy=policy.default).parse(f)


def received_hops(message):
    """Return the Received: headers oldest-first (the order the email travelled)."""
    hops = message.get_all("Received")
    if hops is None:
        return []
    return list(reversed(hops))