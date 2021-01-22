package com.smbs.serverlet;

import com.smbs.dao.UserDao;
import com.smbs.mod.Student;

import java.io.IOException;


@javax.servlet.annotation.WebServlet("/register")
public class RegisterServerlet extends javax.servlet.http.HttpServlet {
    protected void doPost(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        request.setCharacterEncoding("utf-8");
        String userID = request.getParameter("userID");
        String passWord = request.getParameter("passWord1");
        String userName = request.getParameter("userName");
        UserDao userDao = new UserDao();
        Student stu = userDao.selectById(userID);
        String pwd = stu.getPassword();
        if (pwd == null){
            Student u = new Student();
            u.setUserID(userID);
            u.setPassword(passWord);
            u.setUserName(userName);
            Boolean flag = userDao.addUser(u);
            if(flag){
                response.sendRedirect("registerSuccess.jsp");
            }
        }else{
            response.sendRedirect("registerError.jsp");
        }
    }

    protected void doGet(javax.servlet.http.HttpServletRequest request, javax.servlet.http.HttpServletResponse response) throws javax.servlet.ServletException, IOException {
        doPost(request, response);
    }
}
