import argparse
import logging
import re
from subprocess import check_output, CalledProcessError

logger = logging.getLogger()

branch_name_regex = r'(?:feature|hotfix|bugfix|chore)/(\d+)-.+'
msg_template = "{msg} {issue_id}"

def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Commit message file path')
    parser.add_argument(
        '--branch-name-regex',
        default=branch_name_regex,
        help=f'Regex to extract issue ID from branch name'
    )
    parser.add_argument(
        '--msg-template',
        default=msg_template,
        help=f'Message template'
    )
    args = parser.parse_args(argv)

    commit_msg_file_path = args.filename

    try:
        branch_name = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip().decode()
    except CalledProcessError:
        logger.warning("Cannot get current HEAD, maybe rebase is in progress?")
        return 0

    matched = re.match(args.branch_name_regex, branch_name)

    if matched:
        issue_id = matched.group('issue_id')
        if issue_id.isdigit():
            issue_id = f"#{issue_id}"

        with open(commit_msg_file_path, 'r+') as fh:
            commit_msg = fh.read()
            if issue_id in commit_msg:
                logger.warning("Issue ID already found in commit message")
                return 0

            fh.seek(0, 0)
            fh.write(args.msg_template.format(msg=commit_msg, issue_id=issue_id))

    return 0


if __name__ == '__main__':
    exit(main())
