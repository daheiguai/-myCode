package com.smbs.dao;

import com.smbs.mod.Goods;
import com.smbs.utils.JdbcUtil;

import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.util.ArrayList;
import java.util.List;


public class GoodsDao {
    /**
     * 添加商品
     * @param g
     * @return
     */
    public Boolean addGoods(Goods g) {
        boolean flag = true;
        Connection conn = null;
        PreparedStatement ps = null;

        try{
            conn = JdbcUtil.getConnection();
            String sql = "insert into goods(goodsName,goodsPrice,goodsDescription,userName) values(?,?,?,?)";
            ps =conn.prepareStatement(sql);
            ps.setString(1,g.getGoodsName());
            ps.setInt(2,g.getGoodsPrice());
            ps.setString(3,g.getGoodsDiscription());
            ps.setString(4,g.getUserName());

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
     * 查询所有商品
     * @return
     */
    public List<Goods> getAllGoods() {
        List<Goods> goodsList = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        try{
            conn = JdbcUtil.getConnection();
            String sql = "select * from goods order by goodsID";
            ps =conn.prepareStatement(sql);
            ResultSet resultSet = ps.executeQuery();
            while (resultSet.next()){
                Goods g = new Goods();
                g.setGoodsID(resultSet.getInt("goodsID"));
                g.setGoodsName(resultSet.getString("goodsName"));
                g.setGoodsPrice(resultSet.getInt("goodsPrice"));
                g.setGoodsDiscription(resultSet.getString("goodsDescription"));
                g.setUserName(resultSet.getString("userName"));
                goodsList.add(g);
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
        return goodsList;
    }

    /**
     * 查询所有免费的商品
     * @return
     */
    public List<Goods> getFreeGoods() {
        List<Goods> goodsList = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        try{
            conn = JdbcUtil.getConnection();
            String sql = "select * from goods where goodsPrice = 0 order by goodsID";
            ps =conn.prepareStatement(sql);
            ResultSet resultSet = ps.executeQuery();
            while (resultSet.next()){
                Goods g = new Goods();
                g.setGoodsID(resultSet.getInt("goodsID"));
                g.setGoodsName(resultSet.getString("goodsName"));
                g.setGoodsPrice(resultSet.getInt("goodsPrice"));
                g.setGoodsDiscription(resultSet.getString("goodsDescription"));
                g.setUserName(resultSet.getString("userName"));
                goodsList.add(g);
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
        return goodsList;
    }


    /**
     * 查询所有 该用户的商品
     * @return
     */
    public List<Goods> getMyGoods(String userName) {
        List<Goods> goodsList = new ArrayList<>();
        Connection conn = null;
        PreparedStatement ps = null;
        try{
            conn = JdbcUtil.getConnection();
            String sql = "select * from goods where userName = "+"'"+userName +"'"+ " order by goodsID";
            ps =conn.prepareStatement(sql);
            ResultSet resultSet = ps.executeQuery();
            while (resultSet.next()){
                Goods g = new Goods();
                g.setGoodsID(resultSet.getInt("goodsID"));
                g.setGoodsName(resultSet.getString("goodsName"));
                g.setGoodsPrice(resultSet.getInt("goodsPrice"));
                g.setGoodsDiscription(resultSet.getString("goodsDescription"));
                g.setUserName(resultSet.getString("userName"));
                goodsList.add(g);
            }
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
        return goodsList;
    }



    /**
     * 根据id删除物品
     * @param goodsID
     */
    public void deleteGoods(String goodsID) {
        Connection conn = null;
        PreparedStatement ps = null;
        try{
            conn = JdbcUtil.getConnection();
            String sql = "delete from goods where goodsID = ?";
            ps =conn.prepareStatement(sql);
            ps.setString(1,goodsID);
            ps.executeUpdate();
        }catch (Exception e){
            e.printStackTrace();
        }finally {
            JdbcUtil.close(ps,conn);
        }
    }
}
