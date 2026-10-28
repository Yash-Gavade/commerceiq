-- Run as database administrator on commerceiq360.
-- Query 1: confirm all analytics columns and types.
SELECT table_name, ordinal_position, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'analytics'
ORDER BY table_name, ordinal_position;

-- Query 2: find possible GMV, price, freight and sales columns.
SELECT table_name, column_name, data_type
FROM information_schema.columns
WHERE table_schema = 'analytics'
 AND (column_name ILIKE '%price%' OR column_name ILIKE '%gmv%'
      OR column_name ILIKE '%revenue%' OR column_name ILIKE '%amount%'
      OR column_name ILIKE '%freight%' OR column_name ILIKE '%total%')
ORDER BY table_name, ordinal_position;

-- Query 3: inventory of all analytics objects (including views/materialized views).
SELECT n.nspname AS schema_name, c.relname AS object_name, c.relkind
FROM pg_class c JOIN pg_namespace n ON n.oid = c.relnamespace
WHERE n.nspname = 'analytics' AND c.relkind IN ('r','v','m','p')
ORDER BY c.relname;
