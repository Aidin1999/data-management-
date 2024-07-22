

    SELECT
        `datetime`, `site name`, MAX(`NOx`) AS `maxnox`#selecting a desire out put
    FROM
        `station`,#selecting right schema
        `read`
    WHERE
        YEAR(`datetime`) = 2022 AND `station`.`site_id` = `read`.`site_id_fk`;#by this way the keys are connected and year is 2022
