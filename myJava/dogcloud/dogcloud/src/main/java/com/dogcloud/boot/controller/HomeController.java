package com.dogcloud.boot.controller;

import com.dogcloud.boot.domain.User;
import com.dogcloud.boot.service.HomeService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.Model;
import org.springframework.web.bind.annotation.RequestMapping;

import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServletRequest;

@Controller
public class HomeController {

    @Autowired
    HomeService service;

    User user = null;

    @RequestMapping("/showHome")
    public Object showHome(HttpServletRequest request, Model modle){
        Cookie[] cookies = request.getCookies();
        user = null;
        if (cookies== null) return "redirect:/welcome";
        for (Cookie cookie : cookies) {
            if (cookie.getName().equals("user")){
                user = service.getUser(cookie.getValue());
                break;
            }
        }
        if (user == null) return "redirect:/welcome";
        return "home";
    }

    @RequestMapping("/showHome_left")
    public Object showHome_left(Model model){
        model.addAttribute("user",user);
        return "home_left";
    }
    @RequestMapping("/showHome_top")
    public Object showHome_top(){

        return "home_top";
    }
    @RequestMapping("/showHome_mid")
    public Object showHome_mid(){

        return "home_mid";
    }
}
