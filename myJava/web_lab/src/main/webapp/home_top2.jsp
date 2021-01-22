<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<!DOCTYPE html>
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <title></title>
    <link type="text/css" rel="stylesheet" href="css/css.css" />
</head>
<body >
        <ul class="menu">&nbsp;&nbsp;&nbsp;&nbsp;
            <li><a href="getAllGoods" target="mainFrame">全部物品</a></li>
            <li><a href="getFreeGoods" target="mainFrame">免费清单</a></li>
            <li><a href="getMyGoods?userName=${sessionScope.student.userName}" target="mainFrame">我的物品</a></li>
        </ul>

</body>
</html>
