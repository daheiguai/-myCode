package com.smbs.serverlet;

import com.smbs.dao.GoodsDao;
import com.smbs.mod.Goods;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/addGoods")
public class AddGoods extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String userName = request.getParameter("userName");
        String goodsName = request.getParameter("goodsName");
        String goodsPrice = request.getParameter("goodsPrice");
        String goodsDescription = request.getParameter("goodsDescription");
        Goods g = new Goods();
        g.setGoodsName(goodsName);
        g.setGoodsPrice(Integer.parseInt(goodsPrice));
        g.setGoodsDiscription(goodsDescription);
        g.setUserName(userName);
        GoodsDao goodsDao = new GoodsDao();
        Boolean flag = goodsDao.addGoods(g);
        if (flag){
            request.getRequestDispatcher("getMyGoods").forward(request,response);
        }
        else
            response.sendRedirect("error_add.html");
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}