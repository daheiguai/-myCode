package com.smbs.serverlet;

import com.smbs.dao.GoodsDao;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

@WebServlet("/deleteGoods")
public class DeleteGoods extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String goodsID = request.getParameter("goodsID");
        String userName = request.getParameter("userName");
        GoodsDao goodsDao = new GoodsDao();
        goodsDao.deleteGoods(goodsID);
        request.getRequestDispatcher("getMyGoods").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}