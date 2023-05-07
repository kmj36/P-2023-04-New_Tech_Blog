'''
 ## API v1
 # 작성자 : kmj36
 # 작성일 : 2023-05-07
 # History
 # 
 
'''
import sys
import subprocess
try:
    from flask import request
    from flask_restx import Resource, Api, Namespace
except:
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'pip'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'flask'])
    subprocess.check_call([sys.executable, '-m', 'pip', 'install', '--upgrade', 'flask_restx'])
    from flask import request
    from flask_restx import Resource, Api, Namespace

APIv1 = Namespace('APIv1')
'''
    사용자
'''
@APIv1.route('/user')
class User(Resource):
    def get(self): # 사용자목록 조회 (쿼리: 닉네임, 시작날짜, 마지막날짜(기본값: 사용자만든날짜), 마지막로그인조회여부)
        return "getusers"
    def post(self): # 사용자정보 생성
        return "createuser"
    
@APIv1.route('/user/<userid>')
class UserId(Resource):
    def get(self, userid): # userid사용자정보 조회
        return "getuserinfo %s" % userid
    def post(self, userid): # userid사용자정보 변경
        return "modifyuser %s" % userid
    def delete(self, userid): # userid사용자정보 제거
        return "deleteuser %s" % userid
'''
    게시물
'''
@APIv1.route('/post')
class Post(Resource):
    def get(self): # 게시물목록 조회 (쿼리: userid, tagid, 게시물제목, 게시물 내용, 만든 날짜, 시작날짜, 마지막날짜)
        return "getposts"
    def post(self): # 게시물 생성 (필수 json값: 유저 세션)
        return "createpost"
    
@APIv1.route('/post/<int:postid>')
class Postid(Resource):
    def get(self, postid): # postid게시물 조회
        return "getpost %s" % postid
    def post(self, postid): # postid게시물 변경 (필수 json값: 유저 세션)
        return "modifypost" % postid
    def delete(self, postid): # postid게시물 제거 (필수 json값: 유저 세션 [관리자 제외])
        return "deletepost %s" % postid
    
'''
    댓글
'''
@APIv1.route('/comment/<int:postid>')
class Comment(Resource):
    def get(self, postid): # 댓글 조회 (쿼리: )
        return "getcomment %s" % postid
    def post(self, postid): # 댓글 생성 (필수 json값, 쿼리: postid, 유저 세션)
        return "createcomment %s" % postid
    def delete(self, postid): # 댓글 제거 (필수 json값, 쿼리: postid, commentid, 유저 세션 [관리자 제외])
        return "deletecomment %s" % postid