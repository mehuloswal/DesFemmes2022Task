def custom_method(self):
        self.log.info("Running custom_method")
        self.sync_all(self.nodes)
        self.nodes[1].generate(1)
        self.log.info("Awaiting response from node 2")
        self.sync_blocks()
        assert_equal(self.nodes[1].getbestblockhash(), self.nodes[2].getbestblockhash())
