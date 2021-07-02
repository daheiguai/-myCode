package com.dogcloud.boot.dao;

import com.dogcloud.boot.domain.User;
import org.apache.ibatis.annotations.Mapper;
import org.apache.ibatis.annotations.Select;

@Mapper
public interface UserDao {

    @Select("select * from users where loginID = #{longinID}")
    public User findUserByLoginID(String loginID);

}
