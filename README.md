# Stereotheque admin-api

This repo holds services for metadata management for the Stereotheque app.

Tech used:
- Python 3.6+
- Flask
- neomodel (OGM for Neo4j)
- Neo4j

Setup Neo4j:
- Install Neo4j Desktop
- Create a local database v3.5+
- Set password. (default username is neo4j)
- Start database
- Run ./scripts/neo4j/reset_neo4j.sh {your_neo4j_password}
NOTE: Every change in the model should be followed by running this script.
A change in the model means any update to a class that inherits from neomodel


Branching Strategy:
- Branch out of develop git checkout -b {yourname}/{jira_story_id}-{short_description}
- Do your changes & commit. Let's try using descriptive commit messages
- Push to remote git push origin {branch_name}
- Create a PR to develop and add at least 1 reviewer.
- Wait for code review and make necessary changes
- Once approved, merge into develop
- CI/CD pipeline should trigger


