from github import Github
import time


def get_stars_count(owner, repo, access_token, previous_stars_count):
    g = Github(access_token)
    user = g.get_user(owner)

    changes_detected = False

    for repository in user.get_repos():
        stars_count = repository.stargazers_count
        print(f"Repository: {repository.name}, Stars: {stars_count}")

        # Check if the stars count has changed
        if repository.name == repo and stars_count != previous_stars_count.get(repo):
            print(f"The number of stars for {owner}/{repo} has changed! New count: {stars_count}")
            changes_detected = True

        # Update the previous_stars_count
        previous_stars_count[repository.name] = stars_count

    return changes_detected


def main():
    owner = 'G3nt1'
    repo = 'Flask-sport'
    access_token = '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'  # Replace with your actual GitHub access token

    # Initialize a dictionary to store the previous stars count for each repository
    previous_stars_count = {}

    while True:
        try:
            print("Checking repositories for changes...")
            changes_detected = get_stars_count(owner, repo, access_token, previous_stars_count)

            if changes_detected:
                print("Changes detected !!!")

        except Exception as e:
            print(f"An error occurred: {e}")

        # Wait for some time before checking again
        time.sleep(10)


if __name__ == "__main__":
    main()
