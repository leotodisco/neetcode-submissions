class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsSet = set()
        for email in emails:
            localName = email.split("@")[0]
            domain_name = email.split("@")[-1]
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            emailsSet.add(f"{localName}@{domain_name}")

        return len(emailsSet)