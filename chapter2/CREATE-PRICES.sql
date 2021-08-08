CREATE TABLE prices (
       code TEXT,           -- 銘柄コード
       date TEXT,           -- 日付
       open REAL,           -- 初値
       high REAL,           -- 高値
       low REAL,            -- 安値
       close REAL,          -- 終値
       volume INTEGER,      -- 出来高
       PRIMARY KEY(code, date)
);
