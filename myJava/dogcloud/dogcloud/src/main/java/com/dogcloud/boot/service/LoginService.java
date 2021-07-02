package com.dogcloud.boot.service;

import com.dogcloud.boot.dao.UserDao;
import com.dogcloud.boot.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class LoginService {

    public LoginService() {}

    @Autowired
    private UserDao dao;

    public User chekuser(String loginID,String password){
        User user = dao.findUserByLoginID(loginID);
        if (user == null)return null;
        if (user.getPassword().equals(password) ){

            return user;
        }
        return null;
    }
}
