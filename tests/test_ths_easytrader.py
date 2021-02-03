# coding: utf-8
import os
import sys
import time
import unittest

sys.path.append(".")

TEST_CLIENTS = set(os.environ.get("EZ_TEST_CLIENTS", "").split(","))

IS_WIN_PLATFORM = sys.platform != "darwin"


@unittest.skipUnless("ths" in TEST_CLIENTS and IS_WIN_PLATFORM, "skip ths test")
class TestYhClientTrader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import easytrader
        cls._user = easytrader.use("ths")
        cls._user.connect(r'C:\同花顺远航版\transaction\xiadan.exe')
        from easytrader import grid_strategies
        cls._user.grid_strategy = grid_strategies.Xls

    def test_balance(self):
        time.sleep(3)
        result = self._user.balance

    def test_today_entrusts(self):
        result = self._user.today_entrusts

    def test_today_trades(self):
        result = self._user.today_trades

    def test_cancel_entrusts(self):
        result = self._user.cancel_entrusts

    def test_cancel_entrust(self):
        result = self._user.cancel_entrust("123456789")

    def test_invalid_buy(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.buy("511990", 1, 1e10)

    def test_invalid_sell(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.sell("162411", 200, 1e10)

    def test_auto_ipo(self):
        self._user.auto_ipo()


@unittest.skipUnless("ht" in TEST_CLIENTS and IS_WIN_PLATFORM, "skip ht test")
class TestHTClientTrader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import easytrader

        if "ht" not in TEST_CLIENTS:
            return

        # input your test account and password
        cls._ACCOUNT = os.environ.get("EZ_TEST_HT_ACCOUNT") or "your account"
        cls._PASSWORD = os.environ.get("EZ_TEST_HT_PASSWORD") or "your password"
        cls._COMM_PASSWORD = (
            os.environ.get("EZ_TEST_HT_COMM_PASSWORD") or "your comm password"
        )

        cls._user = easytrader.use("ht_client")
        cls._user.prepare(
            user=cls._ACCOUNT, password=cls._PASSWORD, comm_password=cls._COMM_PASSWORD
        )

    def test_balance(self):
        time.sleep(3)
        result = self._user.balance

    def test_today_entrusts(self):
        result = self._user.today_entrusts

    def test_today_trades(self):
        result = self._user.today_trades

    def test_cancel_entrusts(self):
        result = self._user.cancel_entrusts

    def test_cancel_entrust(self):
        result = self._user.cancel_entrust("123456789")

    def test_invalid_buy(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.buy("511990", 1, 1e10)

    def test_invalid_sell(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.sell("162411", 200, 1e10)

    def test_auto_ipo(self):
        self._user.auto_ipo()

    def test_invalid_repo(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.repo("204001", 100, 1)

    def test_invalid_reverse_repo(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.reverse_repo("204001", 1, 100)


@unittest.skipUnless("htzq" in TEST_CLIENTS and IS_WIN_PLATFORM, "skip htzq test")
class TestHTZQClientTrader(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        import easytrader

        if "htzq" not in TEST_CLIENTS:
            return

        # input your test account and password
        cls._ACCOUNT = os.environ.get("EZ_TEST_HTZQ_ACCOUNT") or "your account"
        cls._PASSWORD = os.environ.get("EZ_TEST_HTZQ_PASSWORD") or "your password"
        cls._COMM_PASSWORD = (
            os.environ.get("EZ_TEST_HTZQ_COMM_PASSWORD") or "your comm password"
        )

        cls._user = easytrader.use("htzq_client")

        cls._user.prepare(
            user=cls._ACCOUNT, password=cls._PASSWORD, comm_password=cls._COMM_PASSWORD
        )

    def test_balance(self):
        time.sleep(3)
        result = self._user.balance

    def test_today_entrusts(self):
        result = self._user.today_entrusts

    def test_today_trades(self):
        result = self._user.today_trades

    def test_cancel_entrusts(self):
        result = self._user.cancel_entrusts

    def test_cancel_entrust(self):
        result = self._user.cancel_entrust("123456789")

    def test_invalid_buy(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.buy("511990", 1, 1e10)

    def test_invalid_sell(self):
        import easytrader

        with self.assertRaises(easytrader.exceptions.TradeError):
            result = self._user.sell("162411", 200, 1e10)

    def test_auto_ipo(self):
        self._user.auto_ipo()


if __name__ == "__main__":
    unittest.main(verbosity=2)
