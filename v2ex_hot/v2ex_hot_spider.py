#! usr/bin/env/python
# -*- coding:gbk -*-

import urllib2
import sys
import json
reload(sys)
sys.setdefaultencoding( "utf-8" )
html = urllib2.urlopen('https://www.v2ex.com/api/topics/hot.json')
text = html.read()
f_user = open(sys.argv[1], 'w')
f_node = open(sys.argv[2], 'w')
f_posts = open(sys.argv[3], 'w')
f_raw_data = open(sys.argv[4], 'w')

f_raw_data.write(text)
def get_top_post(raw_json):
    s = json.loads(raw_json)
    for i in xrange(len(s)):
        title = s[i]['title']
        content = s[i]['content']
        content = content.replace('', '\n')
        url = s[i]['url']
        f_posts.write('%s:%s\n%s:%s\n%s:%s\n' %('url', url, 'title', title, 'content', content))
        #user_info
        user = s[i]['member']
        user_id = user['id']
        username = user['username']
        f_user.write('%s:%s\n%s:%s\n' %(
            'user_id', user_id,
            'username', username))
        #node_info
        node = s[i]['node']
        node_id = node['id']
        node_name = node['name']
        node_title = node['title']
        f_node.write('%s:%s\t%s:%s\t%s:%s\n' %(
            'node_id', node_id,
            'node_name', node_name, 
            'node_title', node_title))

if __name__ == '__main__':
    get_top_post(text)

