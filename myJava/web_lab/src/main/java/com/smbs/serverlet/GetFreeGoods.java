package com.smbs.serverlet;

import com.smbs.dao.GoodsDao;
import com.smbs.mod.Goods;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.util.List;

@WebServlet("/getFreeGoods")
public class GetFreeGoods extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        GoodsDao goodsDao = new GoodsDao();
        List<Goods> goodsList =  goodsDao.getFreeGoods();
        request.setAttribute("goodsList",goodsList);
        request.getRequestDispatcher("home_FreeList.jsp").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}
