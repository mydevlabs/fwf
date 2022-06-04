"""Main entrypoint for fwf."""

from argparse import ArgumentError

from absl import app, logging
from absl.flags import argparse_flags


def foo_command(args, unknown):
    """Foo subcommand."""
    logging.info("Bar args %s", args.bar)


def flags_parser(argv):
    """Definition of the CLI parsers."""
    parser = argparse_flags.ArgumentParser(description="fwf CLI", add_help=True)
    subparsers = parser.add_subparsers(description="Subcommands to execute")
    # example with `foo` subcommand
    foo_parser = subparsers.add_parser("foo", description="CLI for foo")
    foo_parser.add_argument("--bar", type=str, required=True, help="bar arg")
    foo_parser.set_defaults(command=foo_command)

    if len(argv) == 1:
        raise ArgumentError("A subcommand must be provided")
    return parser.parse_known_args(argv[1:])


def main(argv):
    """Main function."""
    args, unknown = argv
    args.command(args, unknown)


if __name__ == "__main__":
    app.run(main, flags_parser=flags_parser)
