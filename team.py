#!/usr/local/bin/python3

"""
Team: a lightweight tool for engineering managers.
"""

import argparse


def create_team(cli_args):
    print("Creating %s team: %s" % (cli_args.name, cli_args.note))


def delete_team(cli_args):
    print("Deleting %s team" % cli_args.name)


def get_team_cli_parser():
    team_cli_parser = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    team_subparsers = team_cli_parser.add_subparsers(help="sub-command help")

    # Create a team you are managing. Team performs as a namespace.
    create_team_cmd = team_subparsers.add_parser("create_team", help="Create a team you are managing")
    create_team_cmd.set_defaults(func=create_team)
    create_team_cmd.add_argument("-m", "--name", help="Name of the team")
    create_team_cmd.add_argument("-n", "--note", help="Note of the team")

    # Delete a team you are managing.
    return team_cli_parser


if __name__ == "__main__":
    cli_args_parser = get_team_cli_parser()
    cli_args = cli_args_parser.parse_args()
    cli_args.func(cli_args)
