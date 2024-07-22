
    SELECT
        `site name`, SUM(`vpm2.5`) / COUNT(`vpm2.5`) AS `meanvpm2.5`,
        SUM(`pm2.5`) / COUNT(`pm2.5`) AS `meanpm2.5`,
        SUM(`NOx`) / COUNT(`NOx`) AS `meanNOx`,
        SUM(`NO`) / COUNT(`NO`) AS `meanNO`,
        SUM(`pm10`) / COUNT(`pm10`) AS `meanpm10`,
        SUM(`O3`) / COUNT(`O3`) AS `meanO3`,
        SUM(`NVPM10`) / COUNT(`NVPM10`) AS `meanNVPM10`,
        SUM(`VPM10`) / COUNT(`VPM10`) AS `meanVPM10`,
        SUM(`nvpm2.5`) / COUNT(`nvpm2.5`) AS `meannvpm2.5`,
        SUM(`CO`) / COUNT(`CO`) AS `meanCO`,
        SUM(`RH`) / COUNT(`RH`) AS `meanRH`,
        SUM(`SO2`) / COUNT(`SO2`) AS `meanSO2` #returning diserd out put mean for all subtances
    FROM
        `read`,
        `station` #oldschool join
    WHERE
        YEAR(`datetime`) = 2022 AND HOUR(`datetime`) > 6 AND HOUR(`datetime`) < 10 AND site_id_fk = site_id # forien keys need to be equal to be equal to key in two tables and time also needs to be around 8 
    GROUP BY
        `site name` ;
        #we define every mean by formula of sum of each substances divded by its count and their name as meanof'x' from the joint of tables and conditionig the time        #the site name mean of mentiend subtances are selected and two table are joiend and 
