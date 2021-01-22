<%--
  Created by IntelliJ IDEA.
  User: daheiguai
  Date: 2021/1/5
  Time: 22:28
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<head>
	<title>学生旧物交易平台</title>
	<link rel = "stylesheet" type = "text/css" href = "css/css.css">
</head>

<body>
	<div class="loginbg"></div>
	<p class="login_title">学生旧物信息网</p>
	<div style="position: fixed;top: 16%;width:100%;"><hr size="5" width="100%" color="#881a1f"></div>
	<div class="login1">
		<form  method="post" action="login">
			<div class="login2"><h4>登&nbsp;陆</h4></div>
			<div class="login3"></div>
			<div class="login3">学&nbsp;号：<input type="text" name="userID" class="text"></div>
			<div class="login3">密&nbsp;码：<input type="password" name="passWord" class="text"></div>
			<div class="login3"></div>
			<div class="login3">
				<input type="submit" name="submit" value="登 陆" class="but">
				<input type="button" value="注 册"  onclick="location='register.jsp'" class="but">
			</div>
		</form>
	</div>

</body>
</html>
