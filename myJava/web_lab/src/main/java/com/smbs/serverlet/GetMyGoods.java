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

@WebServlet("/getMyGoods")
public class GetMyGoods extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String userName = request.getParameter("userName");
        GoodsDao goodsDao = new GoodsDao();
        List<Goods> goodsList =  goodsDao.getMyGoods(userName);
        request.setAttribute("goodsList",goodsList);
        request.getRequestDispatcher("home_MyList.jsp").forward(request,response);
    }

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        doPost(request, response);
    }
}