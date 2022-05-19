def testHealth(appClient):
    rv = appClient.get("/health")
    assert rv.status_code == 200