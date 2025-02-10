class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count_map = defaultdict(int)
        
        for entry in cpdomains:
            count, domain = entry.split() 
            count = int(count)
            subdomains = domain.split('.')  
            
            for i in range(len(subdomains)):
                subdomain = ".".join(subdomains[i:])
                count_map[subdomain] += count  
        
        return [f"{cnt} {dom}" for dom, cnt in count_map.items()]

            