import os
import random
from uuid import uuid4

from github import Github


def main() -> None:
    access_token = os.getenv("GITHUB_ACCESS_TOKEN")
    g = Github(access_token)
    repo = g.get_repo("thomasperrot/github-scammer")
    filename = f"{uuid4()}.txt"
    repo.create_file(
        path=f"misc/{filename}",
        message=f"Add {filename}",
        content="\n".join(str(uuid4()) for _ in range(random.randint(1, 30))),
        branch="main",
    )
    print(f"[+] {repo.full_name} successfully updated")


if __name__ == "__main__":
    main()
