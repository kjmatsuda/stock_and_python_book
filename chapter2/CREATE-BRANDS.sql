CREATE TABLE brands (
       code TEXT PRIMARY KEY, -- 銘柄コード
       name TEXT,             -- 銘柄名(正式名称)
       short_name TEXT,       -- 銘柄(略称)
       market TEXT,           -- 上場市場名
       sector TEXT,           -- セクタ
       unit INTEGER   -- 単元株数
);
