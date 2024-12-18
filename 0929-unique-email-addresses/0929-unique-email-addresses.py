class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email = set()

        for i in emails:
            local, domain = i.split("@")
            local = local.split("+")[0]
            local = local.replace(".", "")
            email.add(local + "@" + domain)
        return len(email)