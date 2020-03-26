import argparse
import re
from subprocess import check_output


branch_name_regex = r'(feature|hotfix|bugfix|chore)/(\d+)-.+'


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument('filename', help='Commit message file path')
    args = parser.parse_args(argv)

    commit_msg_file_path = args.filename
    branch_name = check_output(['git', 'symbolic-ref', '--short', 'HEAD']).strip().decode()

    matched = re.match(branch_name_regex, branch_name)

    if matched:
        issue_id = matched.group(2)
        with open(commit_msg_file_path, 'r+') as fh:
            commit_msg = fh.read()
            fh.seek(0, 0)
            fh.write('%s #%s' % (commit_msg, issue_id))

    return 0


if __name__ == '__main__':
    exit(main())
