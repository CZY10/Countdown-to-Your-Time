import itchat

# 登录微信，需要扫描二维码
itchat.auto_login(hotReload=True)

# 查找好友，'FriendName' 是你好友的微信昵称
user = itchat.search_friends(name='金树林天然精油-陈剑')

# 发送消息
user.send('Hello, this is a message from my Python script!')

# 安全退出
itchat.logout()
