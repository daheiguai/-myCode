package com.smbs.serverlet;

import com.smbs.dao.UserDao;
import com.smbs.mod.Student;

import java.io.IOException;

@javax.servlet.annotation.WebServlet("/login")
public class LoginServlet extends javax.servlet.http.HttpServlet {
    protected void doPost(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        String userID = request.getParameter("userID");
        String passWord = request.getParameter("passWord");
        UserDao userDao = new UserDao();
        Student su = userDao.selectById(userID);
        String pwd = su.getPassword();
        if (pwd != null && pwd.equals(passWord)){
            request.getSession().setAttribute("student",su);
            response.sendRedirect("home.jsp");
        }else{
            response.sendRedirect("login.jsp");
        }
    }

    protected void doGet(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        doPost(request, response);
    }
}
