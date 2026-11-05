from typing import Dict, Any
from services.jira_client import get_issue

class RequirementAgent:

    def extract_description(self, issue: Dict[str, Any]):

        description:Dict = issue["fields"].get("description")
        if not description:
            return ""

        text_parts = []
        for block in description.get("content",[]):
            if block.get("type") == "paragraph":
                for item in block.get("content",[]):
                    if item.get("text"):
                        text_parts.append(item["text"])
            elif block.get("type") == "orderedList":
                for list_item in block.get("content", []):
                    for paragraph in list_item.get("content",[]):
                        for item in paragraph.get("content",[]):
                            if item.get("text"):
                                text_parts.append(item["text"])
        return "\n".join(text_parts)

    def process(self, story_id):
        issue = get_issue(story_id)
        description = self.extract_description(issue)
        return {
            "story_id": story_id,
            "summary": issue["fields"]["summary"],
            "requirements": description,
            "priority": issue["fields"]["priority"]["name"],
            "status": issue["fields"]["status"]["name"],
            "story_points": issue["fields"].get("customfield_10016"),
            "labels": issue["fields"]["labels"],
            "test_cases": [],
            "coverage": {},
            "review": {},
            "report": ""
        }

            