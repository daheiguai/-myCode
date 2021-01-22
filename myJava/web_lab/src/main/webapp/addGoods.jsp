<%--
  Created by IntelliJ IDEA.
  User: daheiguai
  Date: 2021/1/8
  Time: 21:00
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <title>添加商品</title>
    <link rel = "stylesheet" type = "text/css" href = "css/css.css">
</head>
<body>
    <div>
    <form method="post" action="addGoods">
        <div class="addG">
            <div class="addG2">发&nbsp;&nbsp;布&nbsp;&nbsp;商&nbsp;&nbsp;品</div>
            <div class="login3"></div>
            <div class="login3">商品名称：<input type="text" name="goodsName"></div>
            <div class="login3">商品价格：<input type="text" name="goodsPrice"></div>
            <div class="login3">商品描述：<textarea name="goodsDescription" style="margin: 0px; height: 78px; width: 275px;"></textarea></div>
            <div class="login3"></div>
            <div class="login3"><input type="submit" name="submit" value="提交" class="but2"></div>
        </div>
        <input name="userName" value="${sessionScope.student.userName}" style="display: none">
    </form>
    </div>
</body>
</html>
