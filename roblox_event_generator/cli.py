#!/usr/bin/env python3
"""
Command-line interface for roblox-event-generator
"""

import argparse
import sys
from pathlib import Path

from .generator import generate


def main():
    """Main CLI entry point"""
    parser = argparse.ArgumentParser(
        description='Generate EventManagerTypes.lua for Roblox projects',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  # Run in current directory (default)
  roblox-event-generator

  # Specify custom source directory
  roblox-event-generator --src-dir game/src

  # Specify custom output path
  roblox-event-generator --output shared/EventManagerTypes.lua
        """
    )

    parser.add_argument(
        '--project-root',
        type=Path,
        default=Path.cwd(),
        help='Root directory of the Roblox project (default: current directory)'
    )

    parser.add_argument(
        '--src-dir',
        type=str,
        default='src',
        help='Source directory relative to project root (default: src)'
    )

    parser.add_argument(
        '--output',
        type=str,
        default='src/ReplicatedStorage/_Libs/EventManagerTypes.lua',
        help='Output file path relative to project root (default: src/ReplicatedStorage/_Libs/EventManagerTypes.lua)'
    )

    parser.add_argument(
        '--version',
        action='version',
        version='%(prog)s 0.1.0'
    )

    args = parser.parse_args()

    try:
        print('Scanning for Events.lua files...')

        num_services, num_events = generate(
            project_root=args.project_root,
            src_dir=args.src_dir,
            output_path=args.output
        )

        print(f'\nFound {num_services} services with {num_events} total events')

        output_file = args.project_root / args.output
        print(f'\nEventManagerTypes.lua has been generated!')
        print(f'Output: {output_file}')

        return 0

    except FileNotFoundError as e:
        print(f'\nError: {e}', file=sys.stderr)
        print('\nMake sure you are running this from your Roblox project root directory.', file=sys.stderr)
        return 1

    except Exception as e:
        print(f'\nUnexpected error: {e}', file=sys.stderr)
        return 1


if __name__ == '__main__':
    sys.exit(main())
