<%--
  Created by IntelliJ IDEA.
  User: daheiguai
  Date: 2021/1/8
  Time: 16:00
  To change this template use File | Settings | File Templates.
--%>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core" %>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title>订单列表</title>
    <link type="text/css" rel="stylesheet" href="css/css.css" />
</head>


<body>
<div class="main">
    <div class="content">
        <table class="list">
            <tr>
                <td>商品号</td>
                <td>商品名称</td>
                <td>商品价格</td>
                <td>商品描述</td>
                <td>卖家</td>
                <td>操作</td>
            </tr>

            <c:forEach items="${requestScope.goodsList}" var="g" >
                <tr>
                    <td>${g.goodsID}</td>
                    <td>${g.goodsName}</td>
                    <td>${g.goodsPrice}</td>
                    <td>${g.goodsDiscription}</td>
                    <td>${g.userName}</td>
                    <td>  <a href="deleteGoods?goodsID=${g.goodsID}&userName=${g.userName}" >删除</a> </td>
                </tr>
            </c:forEach>
        </table>
    </div>
    <input type="button" value="发布商品" onclick="location='addGoods.jsp'">
</div>
</body>
</html>
