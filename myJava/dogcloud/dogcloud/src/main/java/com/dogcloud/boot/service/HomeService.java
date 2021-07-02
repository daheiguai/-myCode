package com.dogcloud.boot.service;

import com.dogcloud.boot.dao.UserDao;
import com.dogcloud.boot.domain.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

@Service
public class HomeService {

    @Autowired
    private UserDao dao;

    public User getUser(String loginID){
        return dao.findUserByLoginID(loginID);
    }

}
