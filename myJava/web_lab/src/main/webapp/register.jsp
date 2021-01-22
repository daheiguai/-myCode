<%--
  Created by IntelliJ IDEA.
  User: daheiguai
  Date: 2021/1/5
  Time: 22:29
  To change this template use File | Settings | File Templates.
--%>

<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>用户注册</title>
    <link rel = "stylesheet" type = "text/css" href = "css/css.css">
</head>

<body >
<div class="loginbg"></div>
<p class="login_title">学生旧物信息网</p>
<div style="position: fixed;top: 16%;width:100%;"><hr size="5" width="100%" color="#881a1f"></div>
<div class="login1">
    <form method="post" action="register" onsubmit="return checkip()" >
        <div class="login2"><h4>注&nbsp;册</h4></div>
        <div class="login3"></div>
        <div class="login3">学&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;号：<input type="text" name="userID" class="text"></div>
        <div class="login3">密&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;码：<input type="password" name="passWord1" class="text"></div>
        <div class="login3">确认密码：<input type="password" name="passWord2" class="text"></div>
        <div class="login3">联系方式：<input type="text" name="userName" class="text"></div>
        <div class="login3">
            <input type="submit" name="submit" value="提交注册" class="but">
        </div>
    </form>
</div>
<script type="text/javascript">
    function checkip() {
        var userid = document.getElementsByName("userID")[0].value;
        if(isNaN(userid)){
            alert('学号全是数字');
            return false;
        }

        var password1 = document.getElementsByName("passWord1")[0].value;
        var password2 = document.getElementsByName("passWord2")[0].value;

        if (password1 != password2){
            alert('两次输入密码不一致！');
            return false;
        }
        else{
            return true;
        }
    }
</script>



</body>
</html>