package com.dogcloud.boot.controller;

import com.dogcloud.boot.domain.User;
import com.dogcloud.boot.service.LoginService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.ResponseBody;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletResponse;
import java.util.HashMap;
import java.util.Map;

@Controller
public class LoginController {

    @RequestMapping("/welcome")
    public String welcome(){
        return "login";
    }


    @Autowired
    LoginService service;


    @RequestMapping(value = "/checkUser")
    @ResponseBody
    public Object login(String userID, String password, HttpServletResponse response){
        User user = service.chekuser(userID,password);
        Map<String,String> map = new HashMap<>();
        if (user == null) {
            System.out.println("账号密码错误");
            response.setStatus(401);
            return "";
        }
        Cookie cookie = new Cookie("user",userID);
        cookie.setMaxAge(60 * 60*24);
        response.addCookie(cookie);
        map.put("msg","登陆成功，正在跳转。。。");
        return map;
    }


}
