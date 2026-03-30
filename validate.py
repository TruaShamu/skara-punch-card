import re

with open('index.html') as f:
    content = f.read()

# Basic checks
assert '<!DOCTYPE html>' in content
assert '</html>' in content
assert content.count('<script>') == content.count('</script>')
assert content.count('<style>') == content.count('</style>')
print('Basic structure OK')

# Check all referenced IDs exist in HTML
get_ids = re.findall(r"getElementById\(['\"]([^'\"]+)['\"]\)", content)
html_ids = re.findall(r'id="([^"]+)"', content)

for gid in sorted(set(get_ids)):
    if gid not in html_ids:
        print(f'WARNING: getElementById("{gid}") - no matching id in HTML')
    else:
        print(f'  OK: {gid}')

print(f'\nJS references {len(set(get_ids))} unique IDs, HTML defines {len(set(html_ids))} IDs')
print('All matched:', all(g in html_ids for g in set(get_ids)))
