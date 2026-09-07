SELECT
    datname,
    ROUND(
    100.0 * blks_hit / NULLIF(blks_hit + blks_read, 0), 2
    ) AS cache_hit_ratio
FROM pg_stat_database
WHERE datname = current_database();