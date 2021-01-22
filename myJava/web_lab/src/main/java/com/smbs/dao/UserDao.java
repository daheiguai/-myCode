package com.smbs.dao;

import com.smbs.mod.Student;
import com.smbs.utils.JdbcUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;


public class UserDao {
    /**
     * 根据id查询用户
     * @param userID
     * @return
     */
    public Student selectById(String userID) {
        Student u = new Student();
        Connection conn = null;
        PreparedStatement ps = null;

        try{
            conn = JdbcUtil.getConnection();
            String sql = "select * from users where  userID = ?";
            ps =conn.prepareStatement(sql);
            ps.setString(1,userID);
            ResultSet resultSet = ps.executeQuery();
            while (resultSet.next()){
                u.setUserName(resultSet.getString("userName"));
                u.setUserID(userID);
                u.setPassword(resultSet.getString("password"));
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
        return u;
    }



    /**
     * 添加用户
     * @param u
     * @return
     */
    public Boolean addUser(Student u) {
        boolean flag = true;
        Connection conn = null;
        PreparedStatement ps = null;

        try{
            conn = JdbcUtil.getConnection();
            String sql = "insert into users(userid,userName,password) values(?,?,?)";
            ps =conn.prepareStatement(sql);
            ps.setString(1,u.getUserID());
            ps.setString(2,u.getUserName());
            ps.setString(3,u.getPassword());
            ps.executeUpdate();
        }catch (Exception e){
            e.printStackTrace();
            flag = false;
        }finally {
            JdbcUtil.close(ps,conn);
        }
        return flag;
    }



    /**
     * 根据id删除用户
     * @param uid
     */
    public void deleteUser(String uid) {
        Connection conn = null;
        PreparedStatement ps = null;
        try{
            conn = JdbcUtil.getConnection();
            String sql = "delete from superUsers where Userid = ?";
            ps =conn.prepareStatement(sql);
            ps.setString(1,uid);
            ps.executeUpdate();
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
    }
}
