package com.dogcloud.boot;

import org.junit.jupiter.api.Test;
import org.springframework.boot.test.context.SpringBootTest;

@SpringBootTest
class DogcloudApplicationTests {

    @Test
    void contextLoads() {
        String a = "wdnm";
        String b = "wdnm";
        System.out.println(a==b);
    }

}
