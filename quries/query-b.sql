
    SELECT
        `site name`, SUM(`vpm2.5`) / COUNT(`vpm2.5`) AS `meanvpm2.5`,
        
        SUM(`pm2.5`) / COUNT(`pm2.5`) AS `meanpm2.5`#returning diserd out put
    FROM
        `read`,
        `station` #joining two tables 
    WHERE
        `site_id_fk` = `site_id` AND YEAR(`datetime`) = 2022 AND HOUR(`datetime`) > 6 AND HOUR(`datetime`) < 10 # forien keys need to be equal to be equal to key in two tables  
    GROUP BY
        `site name` ;
        #the site name mean of mentiend subtances are selected and two table are joiend and 
