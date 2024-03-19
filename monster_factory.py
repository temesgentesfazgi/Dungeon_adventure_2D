from ogre import Ogre
from skeleton import Skeleton
from gremlin import Gremlin
from sql_helper import SQLHelper
import constants


class MonsterFactory:
    """A factory class for creating different types of monsters."""

    def __init__(self, dbFile):
        """
        Initialize the MonsterFactory.

        :param dbFile: The file path of the database containing monster configurations.
        """
        sqlHelper = SQLHelper(dbFile)
        self.monsterConfigs = sqlHelper.load_monster_configs_from_db()

    def create_monster(self, monster_type):
        """
        Create a monster based on the specified type.

        :param monster_type: The type of monster to create.
        :return: An instance of the specified monster type.
        """
        if monster_type == constants.OGRE:
            return self.create_ogre()
        elif monster_type == constants.GREMLIN:
            return self.create_gremlin()
        elif monster_type == constants.SKELETON:
            return self.create_skeleton()
        else:
            return None

    def create_ogre(self):
        """
        Create an Ogre monster using the loaded configurations.

        :return: An instance of the Ogre class.
        """
        ogre_configs = self.monsterConfigs[constants.OGRE]
        return Ogre(ogre_configs[constants.NAME],
                    ogre_configs[constants.HIT_POINTS],
                    ogre_configs[constants.MIN_DAMAGE],
                    ogre_configs[constants.MAX_DAMAGE],
                    ogre_configs[constants.ATTACK_SPEED],
                    ogre_configs[constants.CHANCE_TO_HIT],
                    ogre_configs[constants.CHANCE_TO_HEAL],
                    ogre_configs[constants.MIN_HEAL_POINTS],
                    ogre_configs[constants.MAX_HEAL_POINTS])

    def create_gremlin(self):
        """
        Create a Gremlin monster using the loaded configurations.

        :return: An instance of the Gremlin class.
        """
        gremlin_configs = self.monsterConfigs[constants.GREMLIN]
        return Gremlin(gremlin_configs[constants.NAME],
                       gremlin_configs[constants.HIT_POINTS],
                       gremlin_configs[constants.MIN_DAMAGE],
                       gremlin_configs[constants.MAX_DAMAGE],
                       gremlin_configs[constants.ATTACK_SPEED],
                       gremlin_configs[constants.CHANCE_TO_HIT],
                       gremlin_configs[constants.CHANCE_TO_HEAL],
                       gremlin_configs[constants.MIN_HEAL_POINTS],
                       gremlin_configs[constants.MAX_HEAL_POINTS])

    def create_skeleton(self):
        """
        Create a Skeleton monster using the loaded configurations.

        :return: An instance of the Skeleton class.
        """
        skeleton_configs = self.monsterConfigs[constants.SKELETON]
        return Skeleton(skeleton_configs[constants.NAME],
                        skeleton_configs[constants.HIT_POINTS],
                        skeleton_configs[constants.MIN_DAMAGE],
                        skeleton_configs[constants.MAX_DAMAGE],
                        skeleton_configs[constants.ATTACK_SPEED],
                        skeleton_configs[constants.CHANCE_TO_HIT],
                        skeleton_configs[constants.CHANCE_TO_HEAL],
                        skeleton_configs[constants.MIN_HEAL_POINTS],
                        skeleton_configs[constants.MAX_HEAL_POINTS])
