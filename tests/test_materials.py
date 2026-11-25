"""检查合成资料的关键业务关系，避免错误输入被误作有效资料。"""
import unittest
import numpy as np
from inspect_data import load_materials

class MaterialIntegrity(unittest.TestCase):
    def test_domain_relationships(self):
        v,a=load_materials()
        tree=v['objects']['tree']; children=tree['children']
        names=[c for cs in children.values() for c in cs]
        self.assertEqual(len(names),len(set(names)))
        self.assertNotIn(tree['root'],names)
        for node,weights in zip(v['objects']['parameter_node_order'],a['edge_weight']):
            self.assertEqual(len(children[node]),weights.shape[0])
        anns=v['objects']['annotations']
        self.assertEqual(anns[0]['document_id'],anns[1]['document_id'])
        self.assertNotEqual(anns[0]['annotation_id'],anns[1]['annotation_id'])

if __name__ == '__main__':
    unittest.main()
