import os

from github import Github


def main() -> None:
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(access_token)
    repo = g.get_repo("thomasperrot/github-scammer")
    contents = repo.get_contents("test.txt", ref="test")
    repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch="test")


if __name__ == "__main__":
    main()
