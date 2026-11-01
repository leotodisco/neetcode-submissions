class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        emailsSet = set()
        for email in emails:
            localName, domain_name = email.split("@")
            localName = localName.split("+")[0]
            localName = localName.replace(".", "")
            emailsSet.add(f"{localName}@{domain_name}")

        return len(emailsSet)